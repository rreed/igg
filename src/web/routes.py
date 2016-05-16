def register_routes(app):
    def route(url, view, **kwargs):
        module = view.__module__.split('.')[-1]
        endpoint = '{}.{}'.format(module, view.__name__)
        return app.add_url_rule(url, endpoint, view, **kwargs)

    from .views import index
    route('/', index.show, methods=['GET'])

    from .views import games
    route('/games', games.show, methods=['GET'])
    route('/games/add', games.add, methods=['GET'])
    route('/games', games.create, methods=['POST'])

    from .views import faq
    route('/faq', faq.show, methods=['GET'])

    from .views import crew
    route('/crew', crew.show, methods=['GET'])

    from .views import contact
    route('/contact', contact.show, methods=['GET'])

    from .views import schedule
    route('/schedule', schedule.show, methods=['GET'])

    from .views import interviews
    route('/interviews', interviews.show, methods=['GET'])

    from .views import challenges
    route('/challenges', challenges.show, methods=['GET'])

    from .views import raffles
    route('/raffles', raffles.show, methods=['GET'])
