from app.libs.redprint import Redprint

api = Redprint('book')


@api.route('', methods=['GET'])
def get_book():
    a = 1
    return 'get book'


@api.route('', methods=['POST'])
def create_book():
    return 'create book'
