package silver1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/9205
public class Q9205_WalkingOverDrinks {
    static FastReader scan = new FastReader();

    static class Position {
        int x, y, leftBottle;

        public Position(int x, int y, int leftBottle) {
            this.x = x;
            this.y = y;
            this.leftBottle = leftBottle;
        }
    }

    public static void main(String[] args) {
        int t = scan.nextInt();
        for (int i = 0; i < t; i++) {
            input();
            sol();
        }
    }

    private static void input() {
        storeCnt = scan.nextInt();
        home = new Position(scan.nextInt(), scan.nextInt(), 20);
        for (int i = 0; i < storeCnt; i++) {
            stores[i] = new Position(scan.nextInt(), scan.nextInt(), 0);
            visited[i] = false;
        }
        festivalSpot = new Position(scan.nextInt(), scan.nextInt(), 0);

    }

    private static int getDis(Position p1, Position p2) {
        return Math.abs(p1.x - p2.x) + Math.abs(p1.y - p2.y);
    }

    private static void sol() {
        //bfs
        Queue<Position> q = new LinkedList<>();
        q.add(home);
        int leftBottle = 20;
        while (!q.isEmpty()) {
            {
                Position pos = q.poll();
                if (getDis(pos, festivalSpot) <= leftBottle * 50) {
                    System.out.println("happy");
                    return;
                }
                for (int i = 0; i < storeCnt; i++) {
                    if (visited[i]) {
                        continue;
                    }
                    if (getDis(stores[i], pos) <= leftBottle * 50) {
                        stores[i].leftBottle = 20;
                        q.add(stores[i]);
                        visited[i] = true;
                    }
                }
            }
        }
        System.out.println("sad");
    }

    static int storeCnt;
    static Position home, festivalSpot;
    static Position[] stores = new Position[100];
    static boolean[] visited = new boolean[100];

    static class FastReader {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

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
