from flask import Flask, request

app = Flask(__name__)


@app.route('/guess3', methods=['GET', 'POST'])
def guess3():

    hint_buttons_enabled = """\
                    <input type='submit' name='button' value='za mało'>
                    <input type='submit' name='button' value='za dużo'>
                    <input type='submit' name='button' value='zgadłeś'>
                    """

    hint_buttons_disabled = """\
                    <input type='submit' name='button' value='za mało' disabled>
                    <input type='submit' name='button' value='za dużo' disabled>
                    <input type='submit' name='button' value='zgadłeś' disabled>
                    """

    ending_buttons_visible = f"""\
                    <form action='/guess3' method='GET'>
                        <input type='submit' name='button' value='chcę zagrać jeszcze raz'>
                    </form>
                    <form action='https://github.com/AndrzejSzeszko' method='GET'>
                        <input type='submit' name='button' value='zabierz mnie stąd gdzieś'>
                    </form>
                    """

    def form(try_counter=1, m_counter=0, d_counter=0, minimum=0, maximum=1001,
             hint_buttons=hint_buttons_enabled, message='', ending_message='', ending_buttons=''):
        guess = (int((maximum - minimum) / 2) + minimum)
        return f"""\
            <h2>Pomyśl liczbę od 0 do 1000 a ja zgadnę w maksymalnie dziesięciu próbach.</h2>
            <h4>Gotów?</h4>
            <h4>Zgaduję: {guess} (to jest {try_counter}. próba)</h4>
            <h5>Daj mi wskazówkę:</h5>
                <form action='#' method='POST'>
                    <input type='number' name='guess' value='{guess}' hidden>
                    <input type='number' name='m_counter' value={m_counter} hidden>
                    <input type='number' name='d_counter' value={d_counter} hidden>
                    <input type='number' name='try_counter' value={try_counter} hidden>
                    <input type='number' name='minimum' value={minimum} hidden>
                    <input type='number' name='maximum' value={maximum} hidden>
                    {hint_buttons}
                </form>
                <br>
            <h3>{message}</h3>
            <h3>{ending_message}</h3>
                {ending_buttons}
            """

    if request.method == 'GET':
        return form()
    elif request.method == 'POST':
        try_counter = int(request.form['try_counter'])
        m_counter = int(request.form['m_counter'])
        d_counter = int(request.form['d_counter'])
        minimum = int(request.form['minimum'])
        maximum = int(request.form['maximum'])
        hint_buttons = hint_buttons_enabled
        message = ''
        ending_message = ''
        ending_buttons = ''
        if request.form['button'] == 'za dużo':
            try_counter = int(request.form['try_counter']) + 1
            d_counter = int(request.form['d_counter']) + 1
            maximum = int(request.form['guess'])
        elif request.form['button'] == 'za mało':
            try_counter = int(request.form['try_counter']) + 1
            m_counter = int(request.form['m_counter']) + 1
            minimum = int(request.form['guess'])
        elif request.form['button'] == 'zgadłeś':
            hint_buttons = hint_buttons_disabled
            message = f'Wygrałem za {try_counter}. próbą!'
            ending_message = 'To była ostatnia próba w tej sesji zgadywanki.'
            ending_buttons = ending_buttons_visible
            return form(try_counter, m_counter, d_counter, minimum, maximum, hint_buttons, message,
                        ending_message, ending_buttons)
        if try_counter > 10:
            hint_buttons = hint_buttons_disabled
            ending_message = 'To była ostatnia próba w tej sesji zgadywanki.'
            ending_buttons = ending_buttons_visible
            if (m_counter or d_counter) == 10:
                message = 'Oszuście! Nie możesz podać dziesięć razy pod rząd tej samej wskazówki!'
            else:
                message = 'Oszukujesz!'
            return form(try_counter, m_counter, d_counter, minimum, maximum, hint_buttons, message,
                        ending_message, ending_buttons)
        return form(try_counter, m_counter, d_counter, minimum, maximum, hint_buttons, message,
                    ending_message, ending_buttons)


if __name__ == '__main__':
    app.run(debug=True)
