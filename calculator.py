import numpy as np
from fractions import Fraction


#Konversi nilai float ke pecahan
def to_fraction(value, max_denominator=1000):
    
    try:
        if isinstance(value, (list, np.ndarray)):
            return [to_fraction(v, max_denominator) for v in value]
        if isinstance(value, float):
            frac = Fraction(value).limit_denominator(max_denominator)
            return str(frac)
        return value
    except Exception:
        return value

#PerMatrixan
def perform_matrix_operation(matrix_list, operation):
    if not matrix_list or not operation:
        raise ValueError('Input "matrix" dan "operation" tidak boleh kosong.')

    try:
        matrix = np.array(matrix_list, dtype=float)
    except Exception as e:
        raise ValueError(f'Format matriks tidak valid: {str(e)}')
    
    if operation == 'determinant':
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError(f'Matriks tidak persegi ({matrix.shape[0]}x{matrix.shape[1]}). Tidak bisa menghitung determinan.')
        
        result = np.linalg.det(matrix)
        return to_fraction(result)

    elif operation == 'inverse':
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError(f'Matriks tidak persegi ({matrix.shape[0]}x{matrix.shape[1]}). Tidak bisa di-invers.')

        try:
            result_matrix = np.linalg.inv(matrix)
            return to_fraction(result_matrix.tolist())
        except np.linalg.LinAlgError:
            raise ValueError('Matriks singular, tidak memiliki invers.')

    elif operation == 'transpose':
        result_matrix = matrix.T
        return to_fraction(result_matrix.tolist())
    
    elif operation == 'rank':
        result = np.linalg.matrix_rank(matrix)
        return int(result)

    elif operation == 'kernel':
        u, s, vh = np.linalg.svd(matrix)
        tol = 1e-10
        null_mask = (s <= tol)
        null_space = vh[null_mask].T
        return to_fraction(null_space.tolist())

    elif operation == 'dimension':
        # Dimensi ruang baris = rank
        rank = np.linalg.matrix_rank(matrix)
        rows, cols = matrix.shape
        return {
            'rank': int(rank),
            'nullity': int(cols - rank)
        }

    else:
        raise ValueError(f'Operasi matriks \"{operation}\" tidak dikenal.')
#Operasi Matrix   
def perform_binary_matrix_operation(matrix_a_list, matrix_b_list, operation):
    if not matrix_a_list or not matrix_b_list:
        raise ValueError('Input "Matriks A" dan "Matriks B" tidak boleh kosong.')
    if not operation:
        raise ValueError('Operasi biner (multiply, add, subtract) tidak ditentukan.')

    try:
        matrix_a = np.array(matrix_a_list, dtype=float)
        matrix_b = np.array(matrix_b_list, dtype=float)
    except Exception as e:
        raise ValueError(f'Format matriks tidak valid: {str(e)}')
    
    if operation == 'multiply':
        if matrix_a.shape[1] != matrix_b.shape[0]:
            raise ValueError(
                f'Dimensi tidak valid untuk perkalian. '
                f'Kolom A ({matrix_a.shape[1]}) harus sama dengan Baris B ({matrix_b.shape[0]}).'
            )
        result_matrix = np.dot(matrix_a, matrix_b)

    elif operation == 'add' or operation == 'subtract':
        if matrix_a.shape != matrix_b.shape:
            raise ValueError(
                f'Dimensi tidak valid untuk penjumlahan/pengurangan. '
                f'Dimensi A ({matrix_a.shape}) harus sama dengan Dimensi B ({matrix_b.shape}).'
            )
        
        if operation == 'add':
            result_matrix = np.add(matrix_a, matrix_b)
        else: # operation == 'subtract'
            result_matrix = np.subtract(matrix_a, matrix_b)
            
    else:
        raise ValueError(f'Operasi biner "{operation}" tidak dikenal.')

    return to_fraction(result_matrix.tolist())

# [Sequential Search versi serius dikit-beneran ]

def perform_sequential_search(data_list, target):
    if not isinstance(data_list, list):
        raise ValueError("Data masukan 'data_list' harus berupa list.")
        
    try:
        
        target_num = float(target)
    except ValueError:
        raise ValueError(f"Target '{target}' harus berupa angka.")
    except TypeError:
         raise ValueError("Target tidak boleh kosong.")

    steps = [] 
    found = False
    found_index = -1

    for i, item in enumerate(data_list):
        try:
            item_num = float(item)
            comparison = f"Memeriksa indeks {i} (nilai: {item_num})... "
            
            if item_num == target_num:
                comparison += "DITEMUKAN!"
                steps.append(comparison)
                found = True
                found_index = i
                break 
            else:
                comparison += f"(Bukan {target_num})"
                steps.append(comparison)
        
        except (ValueError, TypeError):
            steps.append(f"Memeriksa indeks {i} (nilai: '{item}')... (Bukan angka, dilewati)")
            continue
    
    return {
        'found': found,
        'index': found_index,
        'target': target_num,
        'steps': steps 
    }