package silver1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

//2:48
public class Q17225_SaehoonsGiftShop {

    static class Order implements Comparable<Order> {
        int time;
        int color;

        public Order(int time, int color) {
            this.time = time;
            this.color = color;
        }
        @Override
        public int compareTo(Order o) {
            if(this.time == o.time) {
                return this.color - o.color;
            }
            return this.time - o.time;
        }
    }

    static FastReader scan = new FastReader();
    static StringBuffer sb = new StringBuffer();

    static void input() {
        sTime = scan.nextInt();
        jTime = scan.nextInt();
        N = scan.nextInt();
        int st = 0;
        int jt = 0;


        for (int i = 0; i < N; i++) {
            String[] next = scan.nextLine().split(" ");
            int t = Integer.parseInt(next[0]);
            int cnt = Integer.parseInt(next[2]);

            int color;
            if (next[1].equals("B")) {
                color = 0;
                if (t > st) {
                    st = t;
                }
                for (int j = 0; j < cnt; j++) {
                    st += j * sTime;
                    pq.add(new Order(st, color));
                }
            } else {
                color = 1;
                if (t > jt) {
                    jt = t;
                }
                for (int j = 0; j < cnt; j++) {
                    jt += j * jTime;
                    pq.add(new Order(jt, color));
                }
            }
        }

        List<Integer> sl = new ArrayList<>();
        List<Integer> jl = new ArrayList<>();
        int num = 0;
        while(!pq.isEmpty()) {
            num += 1;
            Order poll = pq.poll();
            if(poll.color == 0) {
                sl.add(num);
            } else {
                jl.add(num);
            }
        }

        sb.append(sl.size()).append("\n");
        for (int integer : sl) {
            sb.append(integer).append(" ");
        }
        sb.append("\n");
        sb.append(jl.size()).append("\n");
        for (int integer : jl) {
            sb.append(integer).append(" ");
        }
        sb.append("\n");

        System.out.println(sb.toString());
    }

    static int sTime, jTime, N;
    static PriorityQueue<Order> pq = new PriorityQueue<>();

    public static void main(String[] args) {
        input();
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            this.br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while(st == null || !st.hasMoreElements()) {
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
