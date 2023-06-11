""" 8) Escreva um programa que receba três números inteiros quaisquer e apresente: 
a) a soma dos quadrados dos três números;
b) o quadrado da soma dos três números. """

nums = []
for i in range (3) :
    nums.append(int(input("N: ")))
print(f'Soma dos quadrados: {(nums[0] ** 2) + (nums[1] ** 2) + (nums[2] ** 2)}')
print(f'Soma dos três números: {sum(nums)}')