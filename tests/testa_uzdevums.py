
checklist = [('name', 'John', 'John'),
             ('middle_name', '', None),
             ('last_name', 'Smith', ' Smith'),
             ('email', 'johnsmith@example.com', 'john.smith@example.com'),
             ('password', '5f4dcc3b5aa765d61d8327deb882cf99', 'dc647eb65e6711e155375218212b3964'), ]


def compare_fields(checklist):
    errors = list()

    for item in checklist:
        field = item[0]
        expected = item[1] if item[1] else None
        actual = item[2] if item[2] else None

        if expected != actual:
            errors.append(f'Field: {field} \nActual value: {actual} \nExpected value: {expected}\n')

    if errors:
        return '\n' + '\n'.join(errors)
    else:
        return None


def test_list():
    errors = compare_fields(checklist)
    if errors:
        print('Account verification failed:\n' + errors)
    else:
        print('Account verification passed')
