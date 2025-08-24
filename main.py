def main():
    print("Hello from mycrawler!")


if __name__ == "__main__":
    main()
    dic = {
        'a': 1,
        'b': 2,
        'c':{
            'c1': 3
        },
        4: 4
    }
    if '4' in dic:
        print('yes')
    else:
        print('no')

    dataset = set()
    dataset.add(1)
    dataset.add(2)
    dataset.add(1)
    dataset.add('1')
    print(dataset)