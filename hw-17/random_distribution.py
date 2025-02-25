import random

def generate_random_distr(sample_size=100000):
    groups = {f"Group {i*10} - {i*10+9}": 0 for i in range(10)}

    for _ in range(sample_size):
        num = random.randint(0, 99)
        group_index = num // 10
        group_key = f"Group {group_index*10} - {group_index*10+9}"
        groups[group_key] += 1


    print(f"Number of samples: {sample_size}")
    for group, count in groups.items():
        print(f"{group}: {count}")

if __name__ == "__main__":
    generate_random_distr()
