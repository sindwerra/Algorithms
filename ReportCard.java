import java.util.ArrayList;
import java.util.HashMap;

public class ReportCard {

    private String name;                    
    private int studentId;                  
    private String semester;                
    private String year;                    
    private int numOfCourse = 0;            
    private double gradePoints = 0;         
    private double takenCredits = 0;        
    private double semesterGpa = 0;         
    private HashMap<String, Integer> courseIndexer = new HashMap<>();
    private ArrayList<Double> numericalGradeList = new ArrayList<>();
    private ArrayList<String> letterGradeList = new ArrayList<>();
    private HashMap<String, Double> gpaCheckList = new HashMap<>();

    public ReportCard(String studentName, 
                        int studentId, 
                        String curSem,
                        String curYear) {
        this.studentId = studentId;
        name = studentName;
        semester = curSem;
        year = curYear;
        gpaCheckList.put("A", 4.0);
        gpaCheckList.put("A-", 3.7);
        gpaCheckList.put("B+", 3.3);
        gpaCheckList.put("B", 3.0);
        gpaCheckList.put("B-", 2.7);
        gpaCheckList.put("C+", 2.3);
        gpaCheckList.put("C", 2.0);
        gpaCheckList.put("C-", 1.7);
        gpaCheckList.put("D", 1.0);
        gpaCheckList.put("F", 0.0);
    }

    public String getName() {
        return name;
    }

    public int getID(){
        return studentId;
    }

    public String getSemester() {
        return semester;
    }

    public String getYear() {
        return year;
    }

    public int getNumOfCourseTaken() {
        return numOfCourse;
    }

    public double getCredtisTaken() {
        return takenCredits;
    }

    public double getGradePoints() {
        return gradePoints;
    }

    public double getSemGPA() {
        return semesterGpa;
    }

    public boolean addCourseGrade(String courseName, String letterGrade, int courseCredits) {
        if (courseIndexer.containsKey(courseName)) {
            System.out.println("The course is already in report and cannot modify!");
            return false;
        } 
        if (!gpaCheckList.containsKey(letterGrade)) {
            System.out.println("The grade format is incorrect.");
            return false;
        } 
        if (courseCredits <= 0) {
            System.out.println("The credits is illegal.");
            return false;
        } else {
            double numericalGrade = gpaCheckList.get(letterGrade);
            takenCredits += courseCredits;
            gradePoints += (courseCredits * numericalGrade);
            courseIndexer.put(courseName, numOfCourse++);
            semesterGpa = gradePoints / takenCredits;
            numericalGradeList.add(numericalGrade);
            letterGradeList.add(letterGrade);
            return true;
        }
    }

    public String getCourseGrade(String courseName) {
        if (!courseIndexer.containsKey(courseName)) {
            return "This student didn't take this course";
        } else {
            String letterGrade = letterGradeList.get(courseIndexer.get(courseName));
            return name + "\'s grade for course: " + courseName + " is " + letterGrade;
        }
    }

    private String getSemesterGrade() {
        if (numOfCourse == 0) {
            return name + " didn\'t take any course this semester";
        } else {
            String result = "Student: " + name + "\nStudent ID: " + studentId + 
                            "\nYear: " + year + "\nSemester: " + semester + 
                            "\nTaken credits: " + takenCredits + 
                            "\nOverall GPA: " + semesterGpa;
            return result;
        }
    }

    public String toString() {
        return getSemesterGrade();
    }
}
