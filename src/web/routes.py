def register_routes(app):
    def route(url, view, **kwargs):
        module = view.__module__.split('.')[-1]
        endpoint = '{}.{}'.format(module, view.__name__)
        return app.add_url_rule(url, endpoint, view, **kwargs)

    from .views import index
    route('/', index.index, methods=['GET'])

    from .views import games
    route('/games', games.list, methods=['GET'])
    route('/games/add', games.add, methods=['GET'])
    route('/games', games.create, methods=['POST'])