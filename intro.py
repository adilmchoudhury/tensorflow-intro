# Import `tensorflow`
import tensorflow as tf

# Initialize two constants
x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])

# Multiply
result = tf.multiply(x1, x2)



### One way of initializing the Session

# Intialize the Session
sess = tf.Session()

# Print the result
print(sess.run(result))

# Close the session
sess.close()


### another way of using the default Session

# Initialize Session and run 'result'
with tf.Session() as sess:
  output = sess.run(result)
  print(output)