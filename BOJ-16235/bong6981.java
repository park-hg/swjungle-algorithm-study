package gold4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 11:12
public class Q16235_TreeInvestmentTech {
    static FastReader scan = new FastReader();

    static class Info {
        PriorityQueue<Integer> trees = new PriorityQueue<>();
        int status = 0;
        int food = 5;
    }

    static void input() {
        N = scan.nextInt();
        M = scan.nextInt();
        K = scan.nextInt();
        A = new int[N + 2][N + 2];
        I = new Info[N + 2][N + 2];

        for (int i = 0; i < N + 2; i++) {
            for (int j = 0; j < N + 2; j++) {
                I[i][j] = new Info();
                if (i == 0 || i == (N + 1) || j == 0 || j == (N + 1)) {
                    I[i][j].status = -1;
                }
            }
        }

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                A[i][j] = scan.nextInt();
                I[i][j].food = 5;
            }
        }



        for (int i = 0; i < M; i++) {
            int x = scan.nextInt();
            int y = scan.nextInt();
            int z = scan.nextInt();
            I[x][y].trees.add(z);
        }
    }

    static int N, M, K;
    static int[][] A;
    static Info[][] I;
    static int[][] near = new int[][]{{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

    static void sol() {
        for (int i = 0; i < K; i++) {
//            System.out.println("i = " + i);
//            System.out.println("I[1][1].trees = " + I[1][1].trees);
//            System.out.println("I[1][1].food = " + I[1][1].food);
            //봄
            for (int r = 1; r <= N; r++) {
                for (int c = 1; c <= N; c++) {
                    if (I[r][c].trees.size() > 0) {
                        int death = 0;
                        PriorityQueue<Integer> alive = new PriorityQueue<>();
                        Info info = I[r][c];
                        while(!info.trees.isEmpty() && info.food >= info.trees.peek()) {
                            int age = info.trees.poll();
                            info.food -= age;
                            alive.add(age+1);
                        }
                        while(!info.trees.isEmpty()) {
                            death += info.trees.poll() / 2;
                        }
                        info.trees = alive;
                        info.food += death;
                    }
                }
            }

            //가을
            for (int j = 1; j <= N; j++) {
                for (int k = 1; k <= N; k++) {
                    if(I[j][k].trees.size() > 0) {
                        for(int tree: I[j][k].trees) {
                            if(tree % 5 == 0) {
                                for(int[] n : near) {
                                    int n_r = j + n[0];
                                    int n_c = k + n[1];
                                    if(I[n_r][n_c].status != -1) {
                                        I[n_r][n_c].trees.add(1);
                                    }
                                }
                            }
                        }
                    }
                    I[j][k].food += A[j][k];
                }
            }
        }

        int cnt = 0;
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
//                System.out.println("i = " + i);
//                System.out.println("j = " + j);
//                System.out.println("I[i][j].trees = " + I[i][j].trees);
                cnt += I[i][j].trees.size();
            }
        }
        System.out.println(cnt);
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
