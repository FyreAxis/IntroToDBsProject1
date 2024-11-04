using System.ComponentModel.DataAnnotations;

public class Info {
    public int HireeID {
        get;
        set;
    }
    [Required]
    public string? First_Name {
        get;
        set;
    }
    [Required]
    public string? Last_Name {
        get;
        set;
    }
    public string? Suffix {
        get;
        set;
    }
}