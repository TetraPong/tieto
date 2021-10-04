import pytest
import pytest_check as check


@pytest.fixture()
def check_list_data():
    checklist = [('name', 'John', 'John'),
                 ('middle_name', '', None),
                 ('last_name', 'Smith', ' Smith'),
                 ('email', 'johnsmith@example.com', 'john.smith@example.com'),
                 ('password', '5f4dcc3b5aa765d61d8327deb882cf99', 'dc647eb65e6711e155375218212b3964'), ]
    return checklist


def test_compareFields(check_list_data):
    for item in check_list_data:
        field = item[0]
        expected = item[1] if item[1] else None
        actual = item[2] if item[2] else None

        check.equal(expected, actual, 'in ' + f"{field}")
