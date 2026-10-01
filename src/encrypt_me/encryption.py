import encrypt_me.pi as PI

def encrypt(text: str, key: str = "12345678") -> str :
    magic_key = [int(digit) for digit in list(key)]
    
    ascii_list = [ord(character) for character in text]
    
    bin_list = sum([[a + b for a, b in zip(magic_key, bin(val))] for val in ascii_list], [])

    pi_digits = [fib_list()[int(digit)] + int(digit) for digit in PI.digits(num_digits=len(bin_list))] 

    pi_added = [(pi + bin) for pi, bin in zip(pi_digits, bin_list)]
    
    sum_magic = [chr((sum(magic_key) + digit) + 60) for digit in pi_added]
    
    return "".join([str(val) for val in sum_magic])
    

def bin(number: int) -> list[int] :
    bits = []
    tmp = number
    while len(bits) < 8 :
        bits.append(0 if tmp % 2 == 0 else 1)
        tmp //= 2

    return bits[::-1]

def fib_list(n: int = 10) -> list[int] :
    sequence = [0, 1]
    while len(sequence) != n:
        sequence.append(sequence[-1] + sequence[-2])
        
    return sequence
