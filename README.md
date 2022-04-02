# Patient Monitor App
Benjamin Marin EC530 Spring 2022
## Phase 0 COMPLETE
I will have two branches: a main branch and a dev branch. I will work on every phase in the Dev branch and merge it with the Main branch once it has passed all tests.
## Phase 1 COMPLETE
Made the device module interface. It has a function to validate the data coming from a JSON file from a device and make sure it follows the correct schema to be put into a database system. Have functions to read specific keys from the JSON
data that either comes from the server or client devices. Each data field has a
corresponding function that can retrieve each specific key. Also have a helper function to convert file with a .json extension to a python dict to be used in
the program. There is also a unit getter function to get the corresponding SI units for American medical institutes.

Here is an example device JSON.
#### Device JSON Input
<center><img src="/images/exampleDeviceJSON.png" width="80%" /></center>

#### Schema for device Input validation
[Device Schema][1]

## Phase 2 In Progress

## Phase 3 In Progress




------
[1]:../master/deviceSchema.json
