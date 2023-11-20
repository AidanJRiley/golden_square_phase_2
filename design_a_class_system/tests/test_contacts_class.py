import pytest
from lib.contacts_class import *

def test_given_non_string():
    with pytest.raises(Exception) as e:
        contact1 = Contact('Aidan',447532831661)
    error_message = str(e.value)
    assert error_message == 'Both of these values need to be a string!'

def test_contact_exists():
    contact1 = Contact('Aidan','07532831661')
    assert contact1.name == 'Aidan'
    assert contact1.phone_number == '07532831661'

def test_contact_format():
    contact1 = Contact('Aidan','07532831661')
    assert contact1.format_contact() == 'Aidan:07532831661'