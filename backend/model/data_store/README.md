# BaseDriver

- BaseDriver is a base class that defines the interface for Data Drivers.

- A Data Driver is a gateway between the app's BaseObjects and the chosen means of data storage.

- Data Drivers' functionality are to serialize BaseObjects into insertion/update statements and conversely, to unserialize BaseObjects when those records are being retrieved from data storage.

## Architecture Notes:
- Note that Services and the App layer may call Drivers.
- Drivers should not call Services nor the main App layer.
- Drivers may call into BaseObject interface methods.

## Scale/Optimization Notes:
- Method filter_multiple is the only getter defined in the interface.
-- This is because batch loading objects (using plurals) encourages loading
-- objects from data stores using as few roundtrips as possible.
-- This avoids the n + 1 problem which is usually a major scalability issue.
-- TL;DR: Getters that output multiple objects instead of singles are faster.
