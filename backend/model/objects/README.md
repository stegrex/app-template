# BaseObject

- BaseObject is a base class that defines the interface for serializable objects.

- Serialization and unserialization happen in between storage to and retrieval
from data stores, through the BaseDriver interface.

- The BaseDriver interface handles data storage needs and calls into the
BaseObject interface in order to construct data storage commands.

- For example, a MySQL based DataDriver will call into BaseObject.get_table() and
BaseObject.to_db_dictionary() to construct insert/update/select queries for use
in MySQL.

## Architecture Notes:
- BaseObjects are lowest level app data as structs, minimal business logic.
- Do not call from BaseObjects into Drivers or Services. The data represented should be independent of how and where it's stored.
- Best practice for a single BaseObject to correspond to a single data table.

## Scale/Optimization Notes:
- BaseObjects should not include any logic for depending on other data records.
-- For example, User should not include logic for UserWallet.
-- This is to avoid cascading calls that are inefficient. (The n + 1 problem.)
-- An example of this problem would be 10 Users that have 5 UserWallets each.
--- With cascading calls, 1 single batch load of 10 Users will automatically call into 10 x 5 UserWallet calls (not batched) or 10 x 1 batched UserWallet call per User.
--- These work out to 1 + 50 = 51 calls or 1 + 10 calls, respectively.
--- A better approach would be to have the Service layer prepare:
---- 1 single batched load of 10 Users.
---- 1 single batched load of all 50 UserWallets once User IDs are known.
---- Total of only 2 data store roundtrip calls.
--- The batching approach reduces the number of data store round trips required.
- For the sake of reduced latency via reduced number of data store round trips,
    use the Service layer to prepare batched load and caching strategies.
    This allows for complex relationships between objects to be constructed and
    destructed as needed.
