def sample_size(train, test):
    print(
        '''
        Размеры выборок, (объекты, признаки).
        - Обучающая: {}
        - Тестовая: {}
        '''.format(
            train.shape,
            test.shape
        )
    )

