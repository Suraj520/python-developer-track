#Matrix operation class
from typing import Optional
import numpy as np
class MatrixOperation:
    #constructor
    def __init__(self,A,shape_A,B=None,shape_B=None):
        self.A = A
        self.B = B
        self.shape_A = shape_A
        self.shape_B = shape_B

    #Method to initialise result matrix depending upon the operation
    def init_result_matrix(self,operation,transpose_form=None):
        self.operation= operation
        #initialising resultant array to be of ones
        if self.shape_A and  self.shape_B :
            if self.operation =="add":
                self.rows,self.cols = int(self.shape_A[0]), int(self.shape_A[1])
            elif self.operation=="mul" and self.shape_A[1] == self.shape_B[0]:
                self.rows,self.cols = int(self.shape_A[0]),int(self.shape_B[1])
            #initialize a matrix of 1s
            self.result = [[1 for _ in range(self.cols)] for _ in range(self.rows)]

        elif self.shape_A:
            if self.operation =="scalar":
                self.rows,self.cols = int(self.shape_A[0]), int(self.shape_A[1])
                self.result = self.A
            elif self.operation=="transpose" or self.operation=="determinant":
                #since at this moment the input matrix dimension is square, so i am not writing logic for other part, feel free to extend out here by segregating through a nested logic over transpose_choice..
                self.rows,self.cols = int(self.shape_A[0]), int(self.shape_A[1])
                self.result = self.A
        #returning self.result
        return self.result

    #method to perform addition
    def add(self):
        self.init_result_matrix(operation="add")
        if self.shape_A != self.shape_B:
            print("The operation cannot be performed.")
        else:
            #iterate and perform addition of elements in the two matrices and then update their values
            for i in range(self.rows):
                for j in range(self.cols):
                    self.result[i][j]=(self.A[i][j] + self.B[i][j])
                    #print(self.r)
            return self.result

    #method to the output matrix as per the desired format of Output.
    def format_result(self):
        for i in range(self.rows):
            print(' '.join(str(i) for i in self.result[i]))

    #method to perform matrix multiplication
    def matrix_multiplication(self):
        self.init_result_matrix(operation="mul")
        if self.shape_A[1]== self.shape_B[0]:
            self.result = np.dot(self.A,self.B)
            #print(self.result)
            return self.result
        else:
            print("The operation cannot be performed.")
            return

    #method to perform scalar multiplication
    def scalar_multiplication(self,scale):
        self.init_result_matrix(operation="scalar")
        for i in range(self.rows):
            for j in range(self.cols):
                self.A[i][j] = scale*self.A[i][j]
        return self.A

    #method to perform transpose
    def transpose(self,transpose_choice):
        self.transpose_choice = transpose_choice
        self.init_result_matrix(operation="transpose") #, transpose_form = transpose_choice for complex logic
        if self.transpose_choice == "1":
            for i in range(self.rows):
                for j in range(i+1, self.rows):
                    self.result[i][j], self.result[j][i] = self.result[j][i], self.result[i][j]
        elif self.transpose_choice == "2":
            for i in range(self.rows-1):
                for j in range(self.rows-i-1):
                    tmp = self.result[i][j]
                    self.result[i][j]= self.result[self.rows-1 -j][self.rows-1 -i]
                    self.result[self.rows-1 -j][self.rows -1-i] = tmp
            return self.result
        elif self.transpose_choice == "3":
            self.result = np.flip(self.result,axis=1)
        elif self.transpose_choice == "4":
            self.result = np.flip(self.result,axis=0)
        return self.result

    #method to calculate determinant
    def calculate_determinant(self):
        return(np.linalg.det(self.A))

    #method to calculate inverse
    def calculate_inverse(self):
        self.init_result_matrix(operation="transpose")
        det = np.linalg.det(self.A)
        if det!=0:
            self.result= np.linalg.inv(self.A)
            return self.result
        else:
            return ("This matrix doesn't have an inverse.")

#function to fill the matrix given shape of it via STDIN
def fill_matrix(mat_shape):
    rows,cols = int(mat_shape[0]), int(mat_shape[1])
    #initializing a zero matrix
    mat =[]
    #fetching rows as it is via STDIN
    for i in range(rows):
        mat.append(input().split())
    #now iterating and converting each elem in mat to int
    for i in range(rows):
        for j in range(cols):
            mat[i][j] = float(mat[i][j])
    return mat

#display menu
while(True):
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4.Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    choice = input("Your choice: ")

    if choice =="1":
        shape_A = input("Enter size of first matrix: ").split()
        print("Enter first matrix:")
        mat_A = fill_matrix(shape_A)
        shape_B = input("Enter size of second matrix: ").split()
        print("Enter second matrix:")
        mat_B = fill_matrix(shape_B)
        #creating an instance of matrix class
        #creating an instance of MatrixOperation class
        MatrixOps = MatrixOperation(mat_A,shape_A,mat_B,shape_B)
        #output = MatrixOps.add()
        output = MatrixOps.add()
        if output:
            print("The result is:")
            MatrixOps.format_result()

    elif choice =="2":
        #input from stdin followed by output.
        #asking the user to enter the details about shape A
        shape_A = input("Enter size of matrix: ").split()
        print("Enter matrix:")
        mat_A = fill_matrix(shape_A)
        #scale = int(input())
        scale = int(input("Enter constant: "))
        #creating an instance of MatrixOperation class
        MatrixOps = MatrixOperation(mat_A,shape_A)
        #output = MatrixOps.add()
        output = MatrixOps.scalar_multiplication(scale)
        if output:
            print("The result is:")
            MatrixOps.format_result()

    elif choice =="3":
        shape_A = input("Enter size of first matrix: ").split()
        print("Enter first matrix:")
        mat_A = fill_matrix(shape_A)
        shape_B = input("Enter size of second matrix: ").split()
        print("Enter second matrix:")
        mat_B = fill_matrix(shape_B)
        #creating an instance of MatrixOperation class
        MatrixOps = MatrixOperation(mat_A,shape_A,mat_B,shape_B)
        #output = MatrixOps.add()
        output = MatrixOps.matrix_multiplication()
        #if output:
        print("The result is:")
        MatrixOps.format_result()

    elif choice =="4":
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
        transpose_choice = input("Your choice: ")
        shape_A = input("Enter size of matrix: ").split()
        print("Enter matrix:")
        mat_A = fill_matrix(shape_A)
        #creating an instance of Matrix Operation class
        MatrixOps = MatrixOperation(mat_A,shape_A)
        output = MatrixOps.transpose(transpose_choice)
        print("The result is:")
        MatrixOps.format_result()

    elif choice =="5":
        shape_A = input("Enter size of matrix: ").split()
        print("Enter matrix:")
        mat_A = fill_matrix(shape_A)
        #creating an instance of MatrixOperation class
        MatrixOps = MatrixOperation(mat_A,shape_A)
        #output = MatrixOps.add()
        output = MatrixOps.calculate_determinant()
        print("The result is:")
        print(output)

    elif choice =="6":
        shape_A = input("Enter size of matrix: ").split()
        print("Enter matrix:")
        mat_A = fill_matrix(shape_A)
        #creating an instance of MatrixOperation class
        MatrixOps = MatrixOperation(mat_A,shape_A)
        #output = MatrixOps.add()
        output = MatrixOps.calculate_inverse()
        print("The result is:")
        MatrixOps.format_result()

    if choice =="0":
        break
