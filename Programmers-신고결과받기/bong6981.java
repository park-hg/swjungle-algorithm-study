import java.util.*;

public class ResultOfReport {
    public static int[] solution(String[] id_list, String[] report, int k) {
        Map<String, Set<Integer>> dic = new HashMap<>();
        Map<String, Integer> idx = new HashMap<>();

        for (int i = 0; i < id_list.length; i++) {
            String id = id_list[i];
            dic.put(id, new HashSet<>());
            idx.put(id, i);
        }


        for(String r: report) {
            String[] s = r.split(" ");
            dic.get(s[1]).add(idx.get(s[0]));
        }

        int[] answer = new int[id_list.length];
        for(String reported : dic.keySet()) {
            if(dic.get(reported).size() >= k) {
                for(int i:dic.get(reported)) {
                    answer[i] += 1;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new String[]{"muzi", "frodo", "apeach", "neo"}, new String[]{"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"}, 2)));
    }
}
