## autocorrect service


### Run the app
+ Run `up.sh` to run service locally, OR
+ Run `docker-compose up` to run it inside a container

The service will start listening on port 5000.

### Fire requests

For *corrected* words:
```bash
$> curl http://localhost:5000/<intended_string>

```
