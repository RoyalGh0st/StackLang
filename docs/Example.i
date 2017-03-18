/* This is an example program in I. */
/* It takes input, reverses it, and outputs it. */
/* Then it converts each reversed letter to a number (its place in the alphabet), adds them together, and outputs that. */

Object Input {
    CHANNEL_1.Connect(Reverser);
    CHANNEL_2.Connect(LettersToNumbersConverter);
    
    CHANNEL_1_TRANSFER_METHOD = Standard;
    CHANNEL_2_TRANSFER_METHOD = Standard;
    
    getAndSendInput()(Null):{ /* The function that gets input and sends it. Takes no input and returns Null.*/
        str input = getInput("Input please: "); // Get input
        // Send the input along the channels
        CHANNEL_1_SEND(input);
        CHANNEL_2_SEND(input);
    }
}

Object Reverser {
    CHANNEL_1.Connect(Input);
    
    CHANNEL_1_TRANSFER_METHOD = Standard;
    
    reverseInput(str:toReverse)(str):{
        str temp;
        i = 0
        for (letter:toReverse) { // Basically, this is like Python's "for x in y" loop
            temp.concat(letter);
        }
        return(temp);
    }
    
    OnRecieve(CHANNEL_1, Standard)():{ /* A built in function that defines what happens when data is recieved from 
                                              specified channel. Also will cause error if data is not in expected format. */
        print(reverseInput(Recieved[CHANNEL_1]);
    }
}

Object LettersToNumbersConverter {
    CHANNEL_1.Connect(Input);
    
    CHANNEL_1_TRANSFER_METHOD = Standard;
    
    str[] A_to_Z = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 
                    'L', 'l', 'M', 'm', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w',
                    'X', 'x', 'Y', 'y', 'Z', 'z'];
                 
    int[] One_to_26 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16,
                     17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26];
    
    
    LettertoNumTable = ConversionTable(A_to_Z, One_to_26);
    
    int number;
    
    OnRecieve(CHANNEL_1, Standard)():{
        for (letter:(Recieved[CHANNEL_1])) {
            number += LetterToNumTable(letter);
        }
        print(total);
    }
}

Activate(Input.getAndSendInput());
        
            
        
