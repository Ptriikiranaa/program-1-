import random

def display_board(board):
    """Menampilkan papan Tic Tac Toe dengan angka 1-9"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("\n")

def display_positions():
    """Menampilkan template posisi 1-9"""
    print("Posisi angka:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")
    print("\n")

def is_winner(board, player):
    """Cek apakah pemain menang"""
    # Kombinasi pemenang (3 baris, 3 kolom, 2 diagonal)
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Baris
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Kolom
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    
    for combo in winning_combos:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
    return False

def is_board_full(board):
    """Cek apakah papan penuh"""
    return all(cell in ['X', 'O'] for cell in board)

def get_empty_cells(board):
    """Mengembalikan list posisi kosong"""
    return [i for i in range(9) if board[i] not in ['X', 'O']]

def computer_move(board):
    """Logika komputer untuk bermain - dengan blocking dan strategi"""
    empty_cells = get_empty_cells(board)
    
    if not empty_cells:
        return None
    
    # Strategi 1: Cek apakah komputer bisa menang
    for cell in empty_cells:
        board_copy = board.copy()
        board_copy[cell] = 'O'
        if is_winner(board_copy, 'O'):
            return cell
    
    # Strategi 2: Blokir kemenangan manusia
    for cell in empty_cells:
        board_copy = board.copy()
        board_copy[cell] = 'X'
        if is_winner(board_copy, 'X'):
            return cell
    
    # Strategi 3: Ambil posisi tengah jika kosong
    if 4 in empty_cells:
        return 4
    
    # Strategi 4: Ambil posisi sudut jika kosong
    corners = [0, 2, 6, 8]
    corner_options = [c for c in corners if c in empty_cells]
    if corner_options:
        return random.choice(corner_options)
    
    # Strategi 5: Pilih kotak kosong secara acak
    return random.choice(empty_cells)

def play_tic_tac_toe():
    """Main game loop untuk Tic Tac Toe"""
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    print("=" * 40)
    print("SELAMAT DATANG DI TIC TAC TOE!")
    print("=" * 40)
    print("\nAnda bermain sebagai X, Komputer sebagai O")
    display_positions()
    
    current_player = 'X'  # Pemain manusia dimulai lebih dulu
    
    # Main game loop
    while True:
        display_board(board)
        
        if current_player == 'X':
            # Giliran pemain
            print("--- GILIRAN ANDA (X) ---")
            while True:
                try:
                    position = int(input("Masukkan posisi (1-9): "))
                    
                    if position < 1 or position > 9:
                        print("❌ Posisi harus antara 1-9!")
                        continue
                    
                    index = position - 1
                    
                    if board[index] in ['X', 'O']:
                        print("❌ Posisi sudah terisi! Pilih posisi lain.")
                        continue
                    
                    board[index] = 'X'
                    break
                    
                except ValueError:
                    print("❌ Input tidak valid! Masukkan angka 1-9.")
            
            # Cek apakah pemain menang
            if is_winner(board, 'X'):
                display_board(board)
                print("=" * 40)
                print("🎉 ANDA MENANG! Selamat!")
                print("=" * 40)
                return
            
            current_player = 'O'
        
        else:
            # Giliran komputer
            print("--- GILIRAN KOMPUTER (O) ---")
            import time
            time.sleep(1)  # Pause agar terlihat natural
            
            move = computer_move(board)
            
            if move is not None:
                board[move] = 'O'
                print(f"Komputer memilih posisi {move + 1}")
            
            # Cek apakah komputer menang
            if is_winner(board, 'O'):
                display_board(board)
                print("=" * 40)
                print("💻 KOMPUTER MENANG! Anda kalah.")
                print("=" * 40)
                return
            
            current_player = 'X'
        
        # Cek apakah papan penuh (Seri)
        if is_board_full(board):
            display_board(board)
            print("=" * 40)
            print("🤝 HASIL SERI! Tidak ada pemenang.")
            print("=" * 40)
            return

def main():
    """Fungsi utama untuk menjalankan permainan"""
    while True:
        play_tic_tac_toe()
        
        play_again = input("\nMainkan lagi? (y/n): ").lower().strip()
        if play_again != 'y':
            print("Terima kasih telah bermain! Sampai jumpa!")
            break

if __name__ == "__main__":
    main()
