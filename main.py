from auth import Signin, Signup
from search import Search

Signin("admin1","admin1")
Signin("pericles","pessoa")

Signup("admin1","admin1","admin1","admin1",["admin2"],["admin2"],["admin2"],["admin2"])
Signup("admin3","admin3","admin3","admin3",["admin2"],["admin2"],["admin2"],["admin2"])

Search("admin1","family")