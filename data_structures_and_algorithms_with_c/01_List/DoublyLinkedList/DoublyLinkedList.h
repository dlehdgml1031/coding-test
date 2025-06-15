#ifndef DOUBLY_LINKEDLIST_H
#define DOUBLY_LINKEDLIST_H

#include <stdio.h>
#include <stdlib.h>

typedef int ElementType;

typedef struct tagNode
{
    ElementType Data;
    struct tagNode* PrevNode;
    struct tagNode* NextNode;
} Node;


// Define func prototype
Node* DLL_CreateNode(ElementType NewData);
Node* DLL_GetNodeAt(Node* Head, int Location);
void DLL_DestoryNode(Node* Node);
void DLL_AppendNode(Node** Head, Node* NewNodw);



#endif