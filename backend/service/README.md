# Services

- Services are classes which represent complex business logic to handle requests
and outputs to the app client.

## Examples of what Services can do:
- Define what data store records will be stored into or retrieved from (Example: Check cache first, then load cold records from MySQL.)
- Construct complex data structures based on app needs. (Example: Construct User and UserWallet into a combined JSON object for an app client to read easily.)
