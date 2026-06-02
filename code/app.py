from flask import Flask, request, abort
import json, rand

app = Flask(__name__)

# Handle the routing for the default '/' route
@app.route('/', methods=['GET'])
def default():
    # Assemble the query parameters into arguments to send to the generator
    args = parse_request_parameters(request.args)

    # Call the generator
    if args['bin_type'] == 'even':  # Even bins
        args['random_numbers'] = rand.generate_even(args['bin_count'], args['range'], args['count'])
    elif args['bin_type'] == 'int':
        args['random_numbers'] = rand.generate_ints(args['range'], args['count'])


    response_json = json.dumps(args)
    print(str(args), response_json)
    return app.response_class(response_json, mimetype='application/json')


def parse_request_parameters(request_args):
    """
    Gets specified keyword arguments if they exist.
    Handles conversion into python types.
    Returns a diction with the converted arguments.
    """
    args = {}
    
    # Gets the requested count of numbers to generate as a string
    request_count = request.args.get('count', 1)
    if request_count is not None:
        try:
            # Attempt to convert the requested count to an integer
            args['count'] = int(request_count)
        except:
            # The requested count is not an integer. Respond with an error code and reason
            abort(400, f"Bad random number count. Requested count (\"{request_count}\") is not an integer.")


    request_range = request.args.get('range', "0,1")
    if request_range is not None:
        split_range =  request_range.split(',')
        if len(split_range) == 1:
            split_range.insert(0, '0')
        
        if len(split_range) == 2:
            try:
                args['range'] = list(map(float, split_range))
            except:
                abort(400, f"Bad random number range. Requested range (\"{request_range}\") cannot be converted to a range of numbers.")
        else:
            abort(400, f"Bad random number range. Requested range (\"{request_range}\") has an incorrect number of arguments. Should be 2.")

    args['bin_type'] = request.args.get('bin_type', 'even')

    args['bin_count'] = int(request.args.get('bin_count', 2))

    return args


if __name__ == '__main__':
    app.run()
