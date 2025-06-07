#include "LinkedList.h"

Node* SLL_CreateNode(ElementType NewData)
{
    Node *NewNode = (Node*)malloc(sizeof(Node));

    NewNode->Data = NewData; // 데이터 저장
    NewNode->NextNode = NULL; // 다음 노드에 대한 포인터 NULL 포인터로 초기화

    return NewNode; // 노드의 주소 반환
}


void SLL_DestroyNode(Node* Node)
{
    free(Node);
}


void SLL_AppendNode(Node** Head, Node* NewNode)
{
    // 헤드 노드가 NULL인 경우 새로운 노드가 Head가 됨
    if ( (*Head) == NULL)
    {
        *Head = NewNode;
    }
    else
    {
        // 테일을 찾아서 NewNode 연결
        Node* Tail = (*Head);
        while (Tail->NextNode != NULL)
        {
            Tail = Tail->NextNode;
        }
        Tail->NextNode = NewNode;
    }
}


Node* SLL_GetNodeAt(Node* Head, int Location)
{
    Node* Current = Head;

    while (Current != NULL && (--Location) >= 0)
    {
        Current = Current->NextNode;
    }
    return Current;
}


void SLL_RemoveNode(Node** Head, Node* Remove)
{
    if ((*Head) == Remove)
    {
        *Head = Remove->NextNode;
    }
    else
    {
        Node* Current = *Head;
        while ( Current != NULL && Current->NextNode != Remove)
        {
            Current = Current->NextNode;
        }

        if ( Current != NULL )
            Current->NextNode = Remove->NextNode;
    }
}


void SLL_InsertAfter(Node* Current, Node* NewNode)
{
    NewNode->NextNode = Current->NextNode;
    Current->NextNode = NewNode; 
}

void SLL_InsertNewHead(Node** Head, Node* NewHead)
{
    if ( (*Head) == NULL )
    {
        (*Head) = NewHead;
    }
    else
    {
        NewHead->NextNode = (*Head);
        (*Head) = NewHead;
    }
}


int SLL_GetNodeCount(Node* Head)
{
    int Count = 0;
    Node* Current = Head;

    while (Current != NULL)
    {
        Current = Current->NextNode;
        Count++;
    }
    return Count;
}

void SLL_InsertBefore(Node**Head, Node* Current, Node* NewNode)
{
    // 1) 리스트가 비어 있거나 Current가 NULL이면 아무 작업도 하지 않음
    if ( (*Head) == NULL || Current == NULL)
    {
        return;
    }

    // 2) Current가 헤드(node == *Head)인 경우 => 새 노드를 곧바로 헤드로 만들기
    if ((*Head) == Current)
    {
        NewNode->NextNode = *Head;
        *Head = NewNode;
        return;
    }

    // 3) Current가 헤드가 아닌 경우: Current 직전 노드(prev)를 찾아서 연결 재구성
    
    Node* Prev = *Head;
    while (Prev != NULL && Prev->NextNode != Current) {
        Prev = Prev->NextNode;
    }
    
    // 4) Prev->NextNode == Current일 때만 삽입. (리스트에 Current가 존재할 때)
    if (Prev != NULL) {
        Prev->NextNode = NewNode;
        NewNode->NextNode = Current;
    }
}

void SLL_DestroyALLNodes(Node** List)
{
    if (List == NULL || *List == NULL) {
        return;  // 이미 빈 리스트이거나 잘못된 인자
    }

    Node* Current = *List;
    Node* NextNode = NULL;

    // 1) 헤드부터 시작해서 순회하면서 free
    while (Current != NULL) {
        NextNode = Current->NextNode;  // 다음 노드 주소를 임시 저장
        free(Current);                // 현재 노드 해제
        Current = NextNode;           // 다음 노드로 이동
    }

    // 2) 최종적으로 헤드를 NULL로 만들어 빈 리스트 상태로 설정
    *List = NULL;
}