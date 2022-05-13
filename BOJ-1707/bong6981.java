//https://www.acmicpc.net/problem/1707
package gold4;

import java.io.*;
import java.util.*;

public class Q1707_BipartiteGraph {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        V = scan.nextInt();
        E = scan.nextInt();
        arr = new ArrayList<>();
        colors = new int[V+1];
        for (int i = 0; i <= V; i++) {
            arr.add(new ArrayList<>());
        }
        for (int j = 0; j < E; j++) {
            int u = scan.nextInt();
            int v = scan.nextInt();
            arr.get(u).add(v);
            arr.get(v).add(u);
        }
    }

    static int T, V, E;
    static List<List<Integer>> arr;
    static int[] colors;

    static boolean dfs(int start, int color) {
        colors[start] = color;
        for(int des : arr.get(start)) {
            if(colors[des] == color) {
                return false;
            }
            if(colors[des] == 0) {
                if(!dfs(des, -color)) {
                    return false;
                }
            }
        }
        return true;
    }

    static void sol() {
        for (int i = 1; i <= V; i++) {
             if(colors[i] == 0) {
                 if(!dfs(i, 1)){
                     sb.append("NO").append("\n");
                     return;
                 };
             }
        }
        sb.append("YES").append("\n");
    }

    public static void main(String[] args) {
        T = scan.nextInt();
        for (int i = 0; i < T; i++) {
            input();
            sol();
        }
        System.out.println(sb.toString());
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
