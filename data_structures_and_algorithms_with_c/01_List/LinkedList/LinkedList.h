#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <stdio.h>
#include <stdlib.h>

typedef int ElementType;

typedef struct tagNode
{
    ElementType Data; // 데이터
    struct tagNode *NextNode; // 다음 노드

} Node;

// Define Func Prototype
Node* SLL_CreateNode(ElementType NewData);
Node* SLL_GetNodeAt(Node* Head, int Location);
void  SLL_DestroyNode(Node* Node);
void  SLL_AppendNode(Node** Head, Node* NewNode);
void  SLL_RemoveNode(Node** Head, Node* Remove);
void  SLL_InsertAfter(Node* Current, Node* NewNode);
void  SLL_InsertNewHead(Node** Head, Node* NewHead);
int   SLL_GetNodeCount(Node* Head);
void  SLL_InsertBefore(Node**Head, Node* Current, Node* NewNode);
void  SLL_DestroyALLNodes(Node** List);

#endif