#include "DoublyLinkedList.h"

Node* DLL_CreateNode(ElementType NewData)
{
    Node* NewNode = (Node*)malloc(sizeof(Node));

    NewNode->Data = NewData;
    NewNode->PrevNode = NULL;
    NewNode->NextNode = NULL;

    return NewNode;
}

void DLL_DestoryNode(Node* Node)
{
    free(Node);
}


void DLL_AppendNode(Node** Head, Node* NewNode)
{
    // 헤드 노드가 NULL인 경우 새로운 노드가 Head가 됨
    if ((*Head) == NULL)
    {
        *Head = NewNode;
    }
    else
    {
        // Tail을 찾아 NewNode 연결
        Node* Tail = (*Head);
        while (Tail->NextNode != NULL)
        {
            Tail = Tail->NextNode;
        }
        Tail->NextNode = NewNode;
        NewNode->PrevNode = Tail; // 기존 Tail을 새로운 Tail의 PrevNode가 가리킴
    }
}


Node* DLL_GetNodeAt(Node* Head, int Location)
{
    Node* Current = Head;
    while (Current != NULL && (--Location) >= 0)
    {
        Current = Current->NextNode;
    }

    return Current;
}


void DLL_RemoveNode(Node** Head, Node* Remove)
{
    
}