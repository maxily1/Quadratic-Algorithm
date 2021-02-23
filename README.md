<h1> Quadratic Algorithm </h1>

<h2> Description </h2>
This algorithm is based on a simple math procedure, sqaure root and raise a number to the power.

<h2>How's the algorithm working?</h2>
<h3> Encode </h3>
* Firstly, We take input of a file \ the message we want to encode.
* Then, we loop through each character of the message (including spaces), and we then turn each character into ASCII number and append it to a list, so it has the ascii code of each character that was in the message we received. 
* Thirdly, we take each number in the list of ascii codes, and do a mathematical procedure named "Square root", and append it to a new list which consists of already encoded ascii codes.
* Last but not least, turn it all into a string and printing the result to the user. 

<h3> Decode </h3>
* There, we do the exact opposite of the encode step. We take the encoded message, split it to a list, so we will have a list made entirely of encoded ascii codes.
* Then, we iterate through each number, we raise the number to the power of 2.
* Round the results so we won't have a situtation where the character 'H' for example will be decoded as character 'G' just because we didn't round the number, Then using ASCII code we turn the numbers into characters. 
* Then append all the characters to a list, and then make a string out of that list, and printing the result to the user. 
