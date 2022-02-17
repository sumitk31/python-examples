from unittest.mock import Mock

# Example One
airport = Mock()
airport.gates = ['A1', 'B1', 'C1', 'D1']
airport.departures = {"Delhi": "12:00PM", "Bangalore": "04:30PM"}

#                  OR
#attrs = {'gates':['A1', 'B1', 'C1', 'D1'],'departures': {"Delhi": "12:00PM", "Bangalore": "04:30PM"}}
#airport.configure_mock(**attrs)

airport.close.return_value = "Closing"
airport.open.side_effect = ["Opening","Already Open"]

print(airport.gates)
print(airport.departures)
print(airport.close())    # Closing
print(airport.open())     # Opening...
print(airport.open())     # Already open

# Example Two

mylist = Mock()

mylist.pop.side_effect = ['1','2','3',IndexError("Pop from empty List")]
#             OR
my2ndlist = Mock()
#my2ndlist.configure_mock(pop.side_effect=['1','2','3',IndexError("Pop from empty List")])

print(mylist.pop())
print(mylist.pop())
print(mylist.pop())
print(mylist.pop())