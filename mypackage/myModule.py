
def top_n(items, n):
    '''
    Return the top n items in an array, in desc order.
    
    Args: 
        items (array) : list or array-like object
        n (int) : number of items to return
        
    Return:
        array : top n items in desc order
        
    Example
        >>> top_n([8,3,4,2], 3)
            [8, 4, 3]
    '''
    
    for i in range(n): #keep sorting untill we have the top n items
        for j in range(len(items)-1-i):
            
            if items[j] > items[j+1]: # if this item is bigger than the next item
                items[j], items[j+1] = items[j+1], items[j]
                
                
                
    # get the last two items
    top_n = items[-n]
    
    
    # Return in descending order
    return top_n[::-1]