// https://www.acmicpc.net/problem/2617
package gold5;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Q2617_FindBeads {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        M = scan.nextInt();
        heavyG = new ArrayList<>();
        lightG = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            heavyG.add(new ArrayList<>());
            lightG.add(new ArrayList<>());
        }
        for (int i = 0; i < M; i++) {
            int heavy = scan.nextInt();
            int light = scan.nextInt();
            heavyG.get(light).add(heavy);
            lightG.get(heavy).add(light);
        }
    }

    static int N, M;
    static List<List<Integer>> heavyG, lightG; //이거 어떻게 했는지 보자 자바 랭커들
    static boolean[] visited;


    static void sol() {
        int mid = (N + 1) / 2;
        int result = 0;
        for (int i = 1; i <= N; i++) {
            visited = new boolean[N + 1];
            if (find(heavyG, i) >= mid) {
                result++;
                continue;
            }
            if (find(lightG, i) >= mid) {
                result++;
            }
        }
        System.out.println(result);
    }

    static int find(List<List<Integer>> graph, int start) {
        visited[start] = true;
        int cnt = 0;
        for (int des : graph.get(start)) {
            if (!visited[des]) {
                cnt += find(graph, des) + 1;
            }
        }
        return cnt;
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

        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new File(s)));
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

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
