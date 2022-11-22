from typing import NewType

UserId = NewType('UserId', int)

ProUserId = NewType('ProUserId', UserId)


def get_user_name(user_id: UserId) -> str:
    return f'user_{user_id}'


if __name__ == '__main__':
    some_id = UserId(123456)

    user_1 = get_user_name(UserId(123))
    user_2 = get_user_name(456)

    print(user_1, user_2)
