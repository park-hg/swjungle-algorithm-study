import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static void input() {
        N = scan.nextInt();
        M = scan.nextInt();
        indegree = new int[N+1];
        graph = new ArrayList<>();

        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            int cnt = scan.nextInt();
            if(cnt == 0) {
                continue;
            }
            int prev = scan.nextInt();
            for (int j = 1; j < cnt; j++) {
                int now = scan.nextInt();
                graph.get(prev).add(now);
                indegree[now]++;
                prev = now;
            }
        }
    }

    static int N, M;
    static int[] indegree;
    static List<List<Integer>> graph;

    static void sol() {
        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            if(indegree[i] == 0) {
                q.add(i);
            }
        }

        List<Integer> ans = new ArrayList<>();
        while(!q.isEmpty()) {
            int now = q.poll();
            ans.add(now);
            for(int des: graph.get(now)) {
                indegree[des]--;
                if(indegree[des] == 0) {
                    q.add(des);
                }
            }
        }

        if(ans.size() < N) {
            System.out.println(0);
        } else {
            for (int i : ans) {
                sb.append(i).append("\n");
            }
            System.out.println(sb.toString());
        }

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
            while( st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        Integer nextInt() {
            return Integer.parseInt(next());
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

