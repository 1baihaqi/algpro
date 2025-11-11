import pandas as pd
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS 
from calculator import perform_matrix_operation, perform_binary_matrix_operation, perform_sequential_search

app = Flask(__name__)
CORS(app)
#Buaya
CSV_FILE_PATH = 'crocodile_dataset (1).csv'
try:
    df = pd.read_csv(CSV_FILE_PATH)
    
    df['Observation ID'] = df['Observation ID'].astype(str)
    
    crocodile_data = df.to_dict('records')
    
    print(f"--- Berhasil memuat {len(crocodile_data)} baris data dari {CSV_FILE_PATH} ---")
except FileNotFoundError:
    print(f"--- ERROR: File '{CSV_FILE_PATH}' tidak ditemukan. ---")
    crocodile_data = []
except Exception as e:
    print(f"--- Terjadi error saat memuat CSV: {e} ---")
    crocodile_data = []

def sequential_search_by_id(data_list, target_id):
    target_id_str = str(target_id)
    for record in data_list:
        if record['Observation ID'] == target_id_str:
            return record
    return None

@app.route('/')
def serve_index():
    """
    Sajikan file index.html dari folder 'static'.
    """
    return send_from_directory('static', 'index.html')

@app.route('/search', methods=['POST'])
def handle_search():
    if not crocodile_data:
        return jsonify({'error': 'Data CSV tidak berhasil dimuat di server.'}), 500

    try:
        data = request.json
        target_id = data.get('target_id')
        
        if not target_id:
            return jsonify({'error': 'Data tidak lengkap. Butuh "target_id".'}), 400
            
        result_record = sequential_search_by_id(crocodile_data, target_id)
        
        if result_record:
            response_data = {
                'found': True,
                'data': result_record,
                'message': f'Data untuk ID {target_id} ditemukan.'
            }
        else:
            response_data = {
                'found': False,
                'message': f'Data untuk ID {target_id} tidak ditemukan.'
            }
        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/calculate/matrix', methods=['POST'])
def handle_matrix_calculation():
    try:
        data = request.json
        print("📥 Data masuk ke /calculate/matrix:", data)
        matrix_list = data.get('matrix') 
        operation = data.get('operation')

        if not matrix_list or not operation:
            return jsonify({'error': 'Harap masukkan matrix (list) dan operation.'}), 400

        result = perform_matrix_operation(matrix_list, operation)
        
        return jsonify({
            'success': True, 
            'result': result, 
            'operation': operation
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Error server: {str(e)}'}), 500

@app.route('/calculate/matrix_binary', methods=['POST'])
def handle_binary_matrix_calculation():
    try:
        data = request.json
        matrix_a_list = data.get('matrix_a')
        matrix_b_list = data.get('matrix_b')
        operation = data.get('operation') 

        if not matrix_a_list or not matrix_b_list:
            return jsonify({'error': 'Harap masukkan Matriks A dan Matriks B.'}), 400
        if not operation:
            return jsonify({'error': 'Parameter "operation" (multiply/add/subtract) tidak ada.'}), 400

        result = perform_binary_matrix_operation(matrix_a_list, matrix_b_list, operation)
        
        return jsonify({
            'success': True,
            'operation': operation,
            'result': result
        }), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Error server: {str(e)}'}), 500  

#  ENDPOINT SEQUENTIAL SEARCH (ini beneran)---
@app.route('/calculate/sequential_search', methods=['POST'])
def handle_sequential_search():
    try:
        data = request.json
        data_list = data.get('data_list') # (list angka dari user)
        target = data.get('target')     # (satu angka dari user)

        if data_list is None or target is None:
            return jsonify({'error': 'Harap masukkan "data_list" (list) dan "target".'}), 400

        # Panggil logika dari calculator.py
        result_data = perform_sequential_search(data_list, target)
        
        return jsonify({
            'success': True,
            'result': result_data 
        }), 200

    except ValueError as e:
        # Menangkap error dari calculator.py (misal: input bukan angka)
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        # Menangkap error server umum
        return jsonify({'error': f'Error server: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)