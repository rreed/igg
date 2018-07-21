def register_routes(app):
    def route(url, view, **kwargs):
        module = view.__module__.split('.')[-1]
        endpoint = '{}.{}'.format(module, view.__name__)
        return app.add_url_rule(url, endpoint, view, **kwargs)

    from .views import index
    route('/', index.show, methods=['GET'])

    from .views import login
    route('/login', login.show, methods=['GET', 'POST'])
    route('/logout', login.logout, methods=['GET'])
    route('/forgot_password', login.forgot_password, methods=['GET', 'POST'])
    route('/reset_password', login.reset_password, methods=['GET', 'POST'])

    from .views import register
    route('/register', register.show, methods=['GET', 'POST'])

    from .views import games
    route('/games', games.show, methods=['GET'])
    route('/games/<game_id>', games.detail, methods=['GET'])
    route('/games/suggest', games.suggest, methods=['GET', 'POST'])
    route('/json/games', games.as_json, methods=['GET'])

    from .views import faq
    route('/faq', faq.show, methods=['GET'])

    from .views import crew
    route('/crew', crew.show, methods=['GET'])

    from .views import contact
    route('/contact', contact.show, methods=['GET'])

    from .views import schedule
    route('/schedule', schedule.show, methods=['GET'])
    route('/json/schedule', schedule.as_json, methods=['GET'])
    route('/ajax/schedulemod', schedule.ajax_create, methods=['POST'])
    route('/ajax/elapsed', schedule.elapsed, methods=['GET'])
    route('/ajax/marathoninfo', schedule.marathon_info, methods=['POST'])

    from .views import interviews
    route('/interviews', interviews.show, methods=['GET'])

    from .views import challenges
    route('/challenges', challenges.show, methods=['GET'])

    from .views import raffles
    route('/raffles', raffles.show, methods=['GET'])

    from .views import donate
    route('/donate', donate.show, methods=['GET', 'POST'])
    route('/roi/<amount>', donate.roi, methods=['GET'])
    route('/donate/thanks', donate.thanks, methods=['GET'])

    from .views import charities
    route('/charities', charities.show, methods=['GET'])

    from .views import profile
    route('/profile', profile.show, methods=['GET'])

    from .views import prizes
    route('/prizes', prizes.list, methods=['GET'])
    route('/prize/<prize_id>', prizes.show, methods=['GET'])
