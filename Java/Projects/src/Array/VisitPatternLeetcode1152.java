package Array;

import java.util.*;

public class VisitPatternLeetcode1152 {
    public List<String> mostVisitedWebsite(String[] username, int[] timestamp, String[] website){
        Map<String, TreeMap<Integer, String>> websiteMap = new HashMap<>();
        for (int i = 0; i < timestamp.length; i++) {
            if(!websiteMap.containsKey(username[i])){
                websiteMap.put(username[i], new TreeMap<>());
            }
            TreeMap<Integer, String> timeMap = websiteMap.get(username[i]);
            timeMap.put(timestamp[i], website[i]);
            websiteMap.put(username[i], timeMap);
        }
        TreeMap<String, Integer> sequenceMap = new TreeMap<String, Integer>();
        for (String user: websiteMap.keySet()){
            TreeMap<Integer, String> timeMap = websiteMap.get(user);
            if(timeMap.size() >= 3){
                List<Integer> timeList = new ArrayList<>(timeMap.keySet());
                List<String> allSeqs = formAllSequences(timeList, timeMap);
                for (String seq: allSeqs){
                    sequenceMap.put(seq, sequenceMap.getOrDefault(seq, 0) + 1);
                }
            }
        }
        String res = String.valueOf(sequenceMap.get(sequenceMap.lastKey()));
        return List.of(res.split("->"));
    }

    private List<String> formAllSequences(List<Integer> timeList, TreeMap<Integer, String> timeMap) {
        List<String> result = new ArrayList<>();
        for (int i = 0; i < timeList.size() - 2; i++) {
            for (int j = i + 1; j < timeList.size() - 1; j++) {
                for (int k = j + 1; k < timeList.size(); k++) {
                    result.add(timeMap.get(timeList.get(i)) + "->" + timeMap.get(timeList.get(j)) + "->" + timeMap.get(timeList.get(k)));
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        String[] username = new String[0];
    }
}
