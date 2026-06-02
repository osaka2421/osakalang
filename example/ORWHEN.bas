HENSU score = INPUT

WHEN score >= 90 DO
    SHOW "excellent"
ORWHEN score >= 80 DO
    SHOW "good"
ORWHEN score >= 70 DO
    SHOW "average"
ORWHEN score >= 60 DO
    SHOW "below average"
OTHERWISE
    SHOW "fail"                  
END