# coding=utf-8
def number():
    count = 0
    for i in range(11, 100):
        first_left = i // 10
        first_right = i % 10

        if first_left == first_right:
            continue

        for j in range(i + 1, 100):
            second_left = j // 10
            second_right = j % 10

            if second_left == second_right:
                continue

            newfirst = first_right * 10 + first_left
            newsecond = second_right * 10 + second_left

            if i * j == newfirst * newsecond:
                print('{} * {} = {} * {}'.format(i, j, newfirst, newsecond))

                count += 1
    print(count)

if __name__ == '__main__':
    number()
