

    static boolean isAnagram(String a, String b) {
        if (a.length() != b.length()) {
            return false;
        }
        else {
            a = a.toLowerCase();
            b = b.toLowerCase();
            for (int i = 0; i < a.length(); i++) {
                char ch = a.charAt(i);
                if (b.indexOf(ch) != -1) {
                    b = b.replaceFirst(ch + "", "");
                } 
                else {
                    return false;
                }
            }
            return b.length() == 0;
        }
    }


