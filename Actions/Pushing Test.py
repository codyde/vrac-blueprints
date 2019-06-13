def handler(context, inputs):
    greeting = "Hello, {0}!".format(inputs["target"])
    print(greeting)

    outputs = {
      "heyyyyy": greeting
    }

    return outputs
