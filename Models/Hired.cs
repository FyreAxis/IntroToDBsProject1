using System.ComponentModel.DataAnnotations;

public class Hired {
    [Key]
    public int HireeID {
        get;
        set;
    }
    [Required]
    public int OrgID {
        get;
        set;
    }
    [Required]
    public int HiringManager {
        get;
        set;
    }
    
}