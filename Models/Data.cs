using System.ComponentModel.DataAnnotations;

public class Data {
    [Key]
    public int HireeID {
        get;
        set;
    }
    [Required]
    [MaxLength(255)]
    public string? Department {
        get;
        set;
    }
    [Required]
    [MaxLength(255)]
    public string? JobTitle {
        get;
        set;
    }
    public int YearsOfExperience {
        get;
        set;
    }
    [MaxLength(255)]
    public string? BachelorsFrom {
        get;
        set;
    }
}