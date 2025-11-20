import math
def decrypt_text(unprocessed_text_list, a, b, c):
    processed_text = [float(num) for num in unprocessed_text_list.split(',')]
    decrypted_values = []
    for y in processed_text:
       A = a
       B = b
       C = c - y
       discriminant = B**2 - 4*A*C
    if discriminant < 0:
        raise ValueError(f"No real roots")
    else:
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-B + sqrt_discriminant) / (2 * A)
        x2 = (-B - sqrt_discriminant) / (2 * A)
        # rounding up
        candidates = [round(x1), round(x2)]
        chosen = None
        for val in candidates:
            if 0 <= val <= 127:
                chosen = val
                break
        if chosen is not None:
            decrypted_values.append(chosen)
        else:
            decrypted_values.append(None)
    finaltext = ''.join(chr(number) for number in decrypted_values)
    return finaltext

