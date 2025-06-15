#include <cstdio>
#include <vector>
#include <queue>
#include <stack>

using namespace std;

class Graph
{
public:
    int nV, nE;
    // 인접리스트를 array of vector로 표현
    // 포인터 사용 이유는 vector의 array이기 때문에 array에서 vector의 값을 접근하기 위해
    vector<int> *edges;

    void Init(const char *_filename)
    {
        FILE *input = fopen(_filename, "r");
        fscanf(input, "%d", &nV);
        fscanf(input, "%d", &nE);
        edges = new vector<int> [nV];
        for (int i = 0; i<nE; i++)
        {
            char a, b;
            fscanf(input, " %c %c", &a, &b);
            int x, y;
            x = a - 'A';
            y = b - 'A';
            edges[x].push_back(y); // push back -> 벡터의 뒤에 데이터 추가 메서드
        }
        fclose(input);
    }
};

void BFS(Graph &_g, int _stIdx = 0)
{
    // Visit flag 생성 및 false 초기화
    bool *visit = new bool [_g.nV];
    for (int i = 0; i < _g.nV; i++)
    {
        visit[i] = false;
    }

    queue<int> q;
    q.push(_stIdx);
    visit[_stIdx] = true; // 첫번째 방문 노드 visit flag true 할당

    while( !q.empty() )
    {
        int x = q.front();
        q.pop();
        printf("%c ", x + 'A');
        
        for(int i = 0; i < _g.edges[x].size(); i++)
        {
            if ( !visit[_g.edges[x][i]] ) // x vertex의 연결 노드 중 방문하지 않은 노드 확인
            {
                q.push(_g.edges[x][i]);
                visit[_g.edges[x][i]] = true;
            }
        }
    }
    delete [] visit;
}

void DFS(Graph &_g, int _stIdx = 0)
{
    bool *visit = new bool [_g.nV];
    for (int i = 0; i < _g.nV; i++)
    {
        visit[i] = false;
    }

    stack<int> s;
    s.push(_stIdx);
    visit[_stIdx] = true; // 첫번째 방문 노드 visit flag true 할당

    while( !s.empty() )
    {
        int x = s.top();
        s.pop();
        printf("%c ", x + 'A');
        
        //for(int i = 0; i < _g.edges[x].size(); i++)
        for (int i = _g.edges[x].size() - 1; i >= 0; i--) // 스택에 역순으로
        {
            if ( !visit[_g.edges[x][i]] ) // x vertex의 연결 노드 중 방문하지 않은 노드 확인
            {
                s.push(_g.edges[x][i]);
                visit[_g.edges[x][i]] = true;
            }
        }
    }
    delete [] visit;
}

int main(int argc, char **argv)
{
    // argv[0]: cmd 입력한 첫 번째 string -> 실행 파일 이름(.exe)
    // argv[1]: cmd 입력한 두 번째 string
    Graph g;
    g.Init( argv[1] );

    printf("\n");
    printf("BFS: ");
    BFS(g);
    printf("\n");

    printf("DFS: ");
    DFS(g);
    printf("\n");

    return 1;
}