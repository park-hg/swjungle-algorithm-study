package gold5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q14503_RobotCleaner {
    static FastReader scan = new FastReader();

    static void input() {
        N = scan.nextInt();
        M = scan.nextInt();
        r = scan.nextInt();
        c = scan.nextInt();
        d = scan.nextInt();
        pos = new Position(r, c, d);
        graph = new int[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                graph[i][j] = scan.nextInt();
            }
        }
    }

    static class Position {
        int r, c;
        int d;

        public Position(int r, int c, int d) {
            this.r = r;
            this.c = c;
            this.d = d;
        }
    }

    static int N, M, r, c, d;
    static int[][] graph;
    static int[][] left = new int[][]{{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
    static int[][] behind = new int[][]{{1, 0}, {0, -1}, {-1, 0}, {0, 1}};
    static Position pos;

    static void sol() {
        int cnt = 0;
        int rotateCnt = 0;

        while (true) {
            if (graph[r][c] == 0) {
                graph[r][c] = -1;
                cnt++;
            }
            graph[r][c] = -1;
            int left_r = r + left[d][0];
            int left_c = c + left[d][1];
            if (0 <= left_r && left_r < N && 0 <= left_c && left_c < M && graph[left_r][left_c] == 0) {
                d = changeDir(d);
                r = left_r;
                c = left_c;
                rotateCnt = 0;
            } else {
                rotateCnt++;
                d = changeDir(d);
                if (rotateCnt == 4) {
                    int behind_r = r + behind[d][0];
                    int behind_c = c + behind[d][1];
                    if (graph[behind_r][behind_c] == 1) {
                        break;
                    } else {
                        r = behind_r;
                        c = behind_c;
                        rotateCnt = 0;
                    }
                }
            }

        }
        System.out.println(cnt);
    }


    static int changeDir(int d) {
        if (d == 0) {
            return 3;
        }
        return d-1;
    }

    public static void main(String[] args) {
        input();
        sol();
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }
}
