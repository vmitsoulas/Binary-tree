# The following assumptions have been made for the definition of a binary tree and its representation in a list:
# 1) Each node has at most two children
# 2) In the list representation of the binary tree the left child is always presented before the right child
# 3) The nodes of the binary tree must have either non-negative values or values of type None
# Example:
'''
arr = [3,9,7,12,14,15,17,20,15]

tree = {
     "value":3,
     "left":{
          "value":9,
          "left":{
               "value":12,
               "left":{
                    "value":20
               },
               "right":{
                    "value":15
               },
          },
          "right":{
               "value":14,
               }
          },
     "right":{
          "value":7,
          "left":{
               "value":15
          },
          "right":{
               "value":17
          }
     }
}
'''
# Objectives:
# a) Compute all permutations of the binary tree
# b) Reduce these permutations by computing the sum of the rightmost weights
# c) Return the list of the reduced weights for all generated permutations, as a comma-separated string
# d) If the input list does not correspond to a valid binary tree return the string "invalid"

# This function checks if the given list represents a valid binary tree
def isBinaryTree(arr):
    for i in range(len(arr)):
        if arr[i]==None:
            if 2*i +1<len(arr):
                if arr[2*i+1] is not None:
                    return False
            if 2*i +2<len(arr):
                if arr[2*i+2] is not None:
                    return False
        if arr[i]is not None and arr[i]<0:
            return False
    return True

# This function converts the list representation of the binary tree 
# to a dictionary representation for ease of handling
def listToBinaryTree(arr,index=0):
           
    if isBinaryTree(arr) == False:
        print("list does not correspond to a binary tree")
        return None
    if index >=len(arr):
        return None
    node = {}
    node['value'] = arr[index]

    left_child = listToBinaryTree(arr,2*index+1)
    if left_child:
         node["left"] = left_child

    right_child = listToBinaryTree(arr,2*index+2)
    if right_child:
         node["right"] = right_child
    return node

# This function computes all the possible permutations and 
# returns a list of those including the original binary tree
def computePremutations(dictTree):
    if dictTree==None:
        return [None]
    if not dictTree.get("left") and not dictTree.get("right"):
        return [dictTree]
    
    leftPermutations = computePremutations(dictTree.get("left"))
    rightPermutations = computePremutations(dictTree.get("right"))

    permutations = []

    for leftPerm in leftPermutations:
        for rightPerm in rightPermutations:
            # original tree
            permutations.append({
                "value": dictTree["value"],
                "left": leftPerm,
                "right": rightPerm
            })

            # permutation (swapped version)
            permutations.append({
                "value": dictTree["value"],
                "left": rightPerm,
                "right": leftPerm                
            })
    
    return permutations

# This function reduces the list of the various permutations by computing the sum of the rightmost weights
def rightmostNodeValue(dictTree):
    if not dictTree:
        return 0
    if not dictTree.get("right"):
        return dictTree["value"]
    if dictTree["value"]==None:
        previous =0
    else:
        previous = dictTree["value"]
    if rightmostNodeValue(dictTree["right"])==None:
        current =0
    else:
        current = rightmostNodeValue(dictTree["right"])
    return previous + current

# This function returns the list of the reduced weights for all generated permutations as a comma-delimited string
def weightSums(permutations):
    sums = [rightmostNodeValue(tree) for tree in permutations]
    sums = sorted(sums)
    return ','.join(map(str,sums))

# Main program that combines all the functions required for the current workflow
def BinaryTreePermutation(arr):
    if isBinaryTree(arr)==False:
        return "invalid"
    
    binaryTree = listToBinaryTree(arr)

    perms = computePremutations(binaryTree)

    permSums = weightSums(perms)

    return permSums


# TestCases
arrSample1 = [3,9,4,None,10]

print(BinaryTreePermutation(arrSample1))

arrSample2 = [3,7,9,12,17,16,15]

print(BinaryTreePermutation(arrSample2))

arrSample3 = [3,7,None,12,17,16,15]

print(BinaryTreePermutation(arrSample3))




 


